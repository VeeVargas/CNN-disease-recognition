import matplotlib.pyplot as plt
import seaborn as sns 
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
plt.style.use('seaborn-pastel')



def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.BuGn):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.subplots(figsize=(6, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap, alpha=.8)
    plt.title(title,  fontsize=20)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, fontsize=15) #rotation=45,
    plt.yticks(tick_marks, classes, fontsize=15, rotation=90)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black", fontsize=15)
    plt.grid(False)
    plt.tight_layout()
    plt.ylabel('True label', fontsize=20)
    plt.xlabel('Predicted label', fontsize=20)


def plot_train_val_epochs(acc, val_acc, loss, val_loss, epochs_range):
    plt.figure(figsize=(16, 6))

    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(fontsize=15)#loc='lower right')
    plt.title('Training and Validation Accuracy', fontsize=20)
    plt.ylabel("Classication Accuracy", fontsize=15)
    plt.xlabel("Epochs", fontsize=15)
    plt.xticks(np.arange(1, 11, step=1))
#     plt.yticks(np.arange(, 1))
    
    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(fontsize=15)#loc='upper right')
    plt.title('Training and Validation Loss', fontsize=20)
    plt.ylabel("Cross Entropy Loss", fontsize=15)
    plt.xlabel("Epochs", fontsize=15)
    plt.xticks(np.arange(1, 11, step=1))

    plt.tight_layout()
    plt.show()


def plot_roc_curve(fpr, tpr):
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(8,6))
    lw = 2
    plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc) #color='darkorange', lw=lw, 
    plt.plot([0, 1], [0, 1], linestyle='--', color='red' ) #, lw=lw, 
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=15)
    plt.ylabel('True Positive Rate', fontsize=15)
    plt.title('Receiver Operating Characteristic', fontsize=20)
    plt.legend(fontsize=15, loc="lower right")
    plt.show()
    

def plot_img_1(img_lst, img_names):
    num = 4
    _axs = range(141,141+num)

    plt.subplots(figsize=(20,8))
    for axis, img, name in zip(_axs, img_lst, img_names):
        plt.subplot(axis), plt.imshow(img);
        plt.title(name, fontsize=15)
        plt.axis('off')
    plt.tight_layout()


def plotImages(images_arr):
    fig, axes = plt.subplots(1, 4, figsize=(20,10))
    axes = axes.flatten()
    for img, ax in zip( images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()